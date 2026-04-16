package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Schema class for a data subject — the individual to whom PII belongs. Links consent records and privacy preferences to the natural person whose data is being processed, enabling subject-centric data models.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PIIPrincipal extends PrivacyStakeholder {

  private List<PrivacyPreference> privacyPreferences;
  private List<ConsentRecord> consentRecords;

}