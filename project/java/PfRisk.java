package example;

/* metamodel_version: 1.12.0 */
/* version: 2024 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A way that handling PII could harm people: where the risk comes from, how likely and how bad it is, and what is done about it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PfRisk  {

  private List<PfPiiItem> pfConcernedPii;
  private List<PfPiiPrincipal> pfConcernedPrincipals;
  private List<PfControl> pfRelatedControls;
  private String pfRiskSource;
  private String pfRiskLikelihood;
  private String pfRiskConsequence;
  private String pfRiskInherentLevel;
  private String pfRiskResidualLevel;
  private String pfRiskOwner;
  private URI pfId;
  private String title;
  private String description;


}