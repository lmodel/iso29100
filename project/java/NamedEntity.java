package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Abstract base class for all entities with a unique identifier, name, and description. Provides common identification and documentation slots.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class NamedEntity  {

  private String id;
  private String name;
  private String description;
  private LocalDate createdDate;
  private LocalDate modifiedDate;

}